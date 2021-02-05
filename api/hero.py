# encoding: utf-8

import flask_restful as restful
from flask import jsonify
from flask_restful import reqparse
from services import Mysql

class Hero(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name" , type=str)
        parser.add_argument("favorite", type=int)
        args = parser.parse_args()

        if args.name is None:
            args.name = ''
        if args.favorite is None:
            args.favorite = ''
        ms = Mysql()
        query = ms.build_query('heros.sql',args.name,args.favorite)
        results = ms.execute_query(query)
        return jsonify({
            "data": results
        })
        
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name" , type=str)
        parser.add_argument("description" , type=str)
        parser.add_argument("image", type=str)
        parser.add_argument("favorite", type=int)
        args = parser.parse_args()
        if args.favorite is None:
            args.favorite = 0
        ms = Mysql()
        query = ms.build_query('postHero.sql',args.name,args.description,args.favorite,args.image)
        results = ms.run_insert(query)
        return jsonify({
            "data": results
        })

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name" , type=str)
        parser.add_argument("description" , type=str)
        parser.add_argument("image", type=str)
        parser.add_argument("favorite", type=int)
        args = parser.parse_args()

        if args.name is None:
            args.name = ''
        if args.description is None:
            args.description = ''
        if args.image is None:
            args.image = ''
        if args.favorite is None:
            args.favorite = 0
        ms = Mysql()
        query = ms.build_query('putHero.sql',args.name,args.description,args.favorite,args.image)
        results = ms.run_insert(query)
        return jsonify({
            "data": results
        })

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name" , type=str)
        args = parser.parse_args()

        if args.name is None:
            args.name = ''
        ms = Mysql()
        query = ms.build_query('deleteHero.sql',args.name)
        results = ms.run_insert(query)
        return jsonify({
            "data": results
        })