import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";

import { Context } from "../store/appContext";

export const Usuario = () => {
	const { store, actions } = useContext(Context);
	const [userInput, setUserInput] = useState([]);
    
    const handleLogout = () => {
        actions.logout();
   
    }

    if (!actions.getToken()){
        return (<h1>Esto es una mierda</h1>);
    };
	return (
        <Link to="/">
		<button onClick={handleLogout} className="btn btn-secondary">Logout</button>
        </Link>
	);
};

