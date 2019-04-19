import React, { Component } from 'react'
import axios from 'axios'

class Data extends Component {
// Make a request for a user with a given ID

componentDidMount() {
    axios.get('http://classqa-api.herokuapp.com/api/list_questions?classroom=databases&id=3')
      .then(function (response) {
        // handle success
        console.log(response);
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .then(function () {
        // always executed
      });
  }

  render () {
      return (<p>Hello</p>)
  }
}

export default Data
