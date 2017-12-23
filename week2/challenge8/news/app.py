from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from pymongo.cursor import Cursor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:xz910815@localhost/shiyanlou'
db = SQLAlchemy(app)

client = MongoClient('127.0.0.1', 27017)
mdb = client.shiyanlou


@app.route('/')
def index():
    file_tar = File.query.all()
    return render_template('index.html', file_tar=file_tar)

    # 显示文章名称的列表
    # 页面中需要显示所有文章的标题（title）列表，此外每个标题都需要使用 `<a href=XXX></a>` 链接到对应的文章内容页面


@app.route('/files/<file_id>')
def file(file_id):
    file_obj = File.query.filter_by(fid=file_id).first()
    try:
        cate_obj = Category.query.filter_by(cid=file_obj.category_id).first()
    except:
        abort(404)
    return render_template('file.html', file_obj=file_obj, cate_obj=cate_obj)

    # file_id 为 File 表中的文章 ID
    #  需要显示 file_id  对应的文章内容、创建时间及类别信息（需要显示类别名称）
    # 如果指定 file_id 的文章不存在，则显示 404 错误页面


@app.errorhandler(404)
def get_error(error):
    return render_template('404.html', restr='shiyanlou 404'), 404


class File(db.Model):
    __tablename__ = 'file'
    fid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    create_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer)
    content = db.Column(db.Text)

    def __init__(self, fid, title, create_time, content, category_id):
        self.fid = fid
        self.title = title
        self.create_time = create_time
        self.content = content
        self.category_id = category_id

    def __repr__(self):
        file_con = dict()
        file_con['fid'] = self.fid
        file_con['title'] = self.title
        file_con['create_time'] = self.create_time
        file_con['content'] = self.content
        file_con['category_id'] = self.category_id
        file_con['tag'] = self.tags
        return file

    def add_tag(self, tag_name):
        mdb.tag.insert({'id': self.fid, 'tag_name': tag_name})

    def rmove_tag(self, tag_name):
        mdb.tag.remove({'tag_name': tag_name})

    @property
    def tags(self):
        tags = []
        result = mdb.tag.find({'id': self.fid})
        for doc in result:
            tags.append(doc['tag'])
        return tags


class Category(db.Model):
    __tablename__ = 'category'
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, cid, name):
        self.cid = cid
        self.name = name

    def __repr__(self):
        return '{}'.format(self.name)

