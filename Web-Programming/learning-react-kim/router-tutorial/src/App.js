import React from 'react';
import { Route, Link } from 'react-router-dom';
import About from './About';
import Home from './Home';
// import Profile from './Profile';
import Profiles from "./Profiles";

const App = () => {
    return (
        <>
        <div>
            <Route path = '/' component={Home} exact={true} />
            <Route path ={['/about', '/info']} component={About} />
            {/*<Route path = '/profile/:username' component={Profile}/>*/}
            <Route path = '/profiles' componet = {Profiles}/>
        </div>
        </>


    );
};
export default App;
