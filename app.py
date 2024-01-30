from flask import Flask, send_from_directory, render_template, abort, request, redirect
import os

app = Flask(__name__)

ITEMS_PER_PAGE = 9

MEDIA_FOLDER = '/media/test_drive'


@app.route('/')
def index():
    return paginate_directory(MEDIA_FOLDER, '')


@app.route('/media/', defaults={'filename': ''})
@app.route('/media/<path:filename>')
def media(filename):
    full_path = os.path.join(MEDIA_FOLDER, filename)
    if os.path.isdir(full_path):
        return paginate_directory(full_path, filename)
    else:
        try:
            return send_from_directory(MEDIA_FOLDER, filename)
        except FileNotFoundError:
            abort(404)


def paginate_directory(directory, current_path):
    page = request.args.get('page', 1, type=int)
    all_files = [os.path.join(current_path, f) for f in os.listdir(directory)]
    total_pages = max(1, ((len(all_files) - 1) // ITEMS_PER_PAGE) + 1)

    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    files = all_files[start:end]

    parent_dir = os.path.dirname(current_path)
    if parent_dir != "" or current_path != "":
        files.insert(0, os.path.join(parent_dir, ".."))

    return render_template('index.html', files=files, current_path=current_path, total_pages=total_pages, current_page=page)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
