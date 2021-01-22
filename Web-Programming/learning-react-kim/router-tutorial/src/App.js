import React from 'react';
import { Route, Link } from 'react-router-dom';
import About from './About';
import Home from './Home';
import Profile from './Profile';
const App = () => {
    return (
        <>
        <div>
            <Route path = '/' component={Home} exact={true} />
            <Route path ={['/about', '/info']} component={About} />
            <Route path = '/profile/:username' component={Profile}/>
        </div>
        </>


    );
};
export default App;
