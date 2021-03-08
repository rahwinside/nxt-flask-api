import pymysql
from app import app, forbidden, internal_server_error
from db_config import mysql
from flask import jsonify, request
import hashlib

from random_string import random_string


@app.route('/register', methods=['POST'])
def POST_endpoint_function():
    try:
        uid = request.form['uid']
        password = request.form['password']
        pager_id = request.form['pager_id']
        name = request.form['name']
        designation = request.form['designation']
        organization = request.form['organization']
        picture = request.form['picture']

        if uid and password and pager_id and name and designation and organization and picture and request.method == 'POST':
            # Generate 28 char API key
            api_key = random_string(28)

            # Hash password to SHA512
            password = hashlib.sha512(password)

            # TODO: Save picture and return picture_url
            picture_url = 'https://vmlinuz.pattarai.in/images/logo_large.png'

            # TODO: Dynamically create bot and get bot_id
            pager_api_key = '1671540030:AAEAMUBDjfS4-w4_DSkct0HQmb23lozGyxo'

            # insert record in database
            try:
                cnx = mysql.connect()
                sql = f"INSERT INTO `nxtstep`.`users` (`uid`, `password`, `api_key`, `pager_id`, `pager_api_key`, `name`, `designation`, `organization`, `picture_url`) VALUES ('{uid}', '{password}', '{api_key}', '{pager_id}', '{pager_api_key}', '{name}', '{designation}', '{organization}', '{picture_url}')"
                cursor = cnx.cursor()
                cursor.execute(sql)
                cursor.close()
                cnx.commit()
                cnx.close()
                json_dict = {"status": "success"}
                res = jsonify(json_dict)
                res.status_code = 200
                return res
            except Exception as e:
                return internal_server_error()
        else:
            return forbidden()

    except Exception as e:
        print(e)
        return internal_server_error()

