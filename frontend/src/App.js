import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
    render() {
        return (
            <div>
                <ReactDemo />
                <Content />
                <FormApp />
                <CheckBox />
            </div>

        );
    }
}
class Content extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            name: "henry bloomberg",
            post: "CEO",
        }
    }
    render() {
        return (
            <div>
                <div id="left_container">
                    <p>this is the left container</p>
                    <h3>{this.props.leftProp}</h3>
                </div>
                <div id="right_container">
                    <p>
                        this is the right container
                    </p>
                    <p>
                        {this.state.name}
                    </p>
                    <p>
                        {this.state.post}
                    </p>
                   <h3>
                       {this.props.rightProp}
                   </h3>
                </div>
            </div>
        );
    }
}
Content.defaultProps = {
    leftProp: "Header from props...",
    rightProp:"Content from props..."
}

class ReactDemo extends React.Component{
    render(){
        return (
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                    <h1 className="App-title">Welcome to Youdecide</h1>
                </header>
                <p className="App-intro">
                    To get started, edit <code>src/App.js</code> and save to reload.
                </p>
                <Content />
            </div>
        );
    }
}

class FormApp extends React.Component {
   constructor(props) {
      super(props);
      
      this.state = {
         data: 'Initial data...'
      }
      this.updateState = this.updateState.bind(this);
   };
   updateState(e) {
      this.setState({data: e.target.value});
   }
   render() {
      return (
         <div>
            <input type = "text" value = {this.state.data} 
               onChange = {this.updateState} />
            <h4>{this.state.data}</h4>
         </div>
      );
   }
}
class CheckBox extends React.Component{

    getInitialState(){
        return {checked: true};
    }

    handlechecked(){
        this.setState({checked:!this.state.checked});
    }

    render(){
            var msg;
            if (this.state.checked){
                msg = "checked"
            }else {
                msg = "unchecked"
            }
           return (
         <div>
            <input type = "checkbox" defaultchecked={this.state.checked}  onchange={this.handlechecked}
                />
            <h4>{msg}</h4>
         </div>
      );
    }
}
export default App;

