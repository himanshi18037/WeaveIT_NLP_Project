from flask import Flask, render_template, url_for, redirect, request, flash
import predictor

app = Flask(__name__)
app.config['SECRET_KEY'] = '612202c1ba464e2083b8287e8a1f5554'

def clean_text(text):
    text = text.replace(" .", ".")
    text = text.replace(" ,", ",")
    text = text.replace(" )", ")")
    text = text.replace("( ", "(")
    text = text.replace(" ;", ";")
    text = text.strip()
    newtext = list(text[0].upper() + text[1:])

    for i in range(len(text)):
        if i < len(text)-2:
            if text[i] == ".":
                newtext[i+2] = newtext[i+2].upper()

    return "".join(newtext)


def get_results(search_query, num_words):
    results = ["abcd", "hello", "abcd"]
    if search_query != "":
        preds = predictor.generate_seq(search_query, num_words)
    #     outputs, query = retrieval_lib.retrieve_patents(search_query)

    #     for i in outputs:
    #         i[2] = clean_text(i[2])
    #         upd = i[2][:500]

    #         if upd != i[2]:
    #             upd = upd + "..."

    #         i[2] = upd
    #         i[3] = clean_text(i[3])

    #     return outputs, query
    return preds

@app.route("/", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def home():
    return render_template("home_page.html")

@app.route("/predictions", methods = ['GET', 'POST'])
def predictions():
    search_query = request.form.get("search_box")
    num_words = request.form.get("num_words")
    if num_words is None:
        num_words = 1
    else:
        num_words = int(num_words)
    
    if search_query is None:
        return render_template("retrieval_page.html", show_hidden = False)

    if len(search_query.split()) < 1:
        return render_template("retrieval_page.html", show_hidden = False)

    if request.method == "POST":
        results =  get_results(search_query, num_words)

        query_var = False
        # if query != search_query:
        #     query_var = True

        if results is not None:
            return render_template("retrieval_page.html", 
                show_hidden = True, search_query = search_query, 
                len = len(results), outputs = results, query_var=query_var)

    return render_template("retrieval_page.html", show_hidden = False)

# punctation marks, random words - Pegasus

if __name__ == "__main__":
    app.run(debug = True)
