#!/usr/bin/node
// prints title of a Star Wars movie where episode number matches given integer

const args = process.argv
const id = args[2]
const url = `https://swapi-api.alx-tools.com/api/films/${id}`

const request = require ('request')
request(url, function(error, response, body){
	console.log(JSON.parse(body).title)
})
