import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";

import { Context } from "../store/appContext";

export const Single = () => {
	const { store, actions } = useContext(Context);
	const [userInput, setUserInput] = useState([]);

	const handleSubmit = (e) => {
        e.preventDefault();
        actions.login(userInput);
        console.log(userInput);
    };
	return (
		<form onSubmit={(e) => handleSubmit(e)}>
			<div className="my-3">
                        <label className="form-label d-flex text-start">
                            <i className="fas fa-envelope mx-2" style={{ color: "#B197FC", fontSize: 24 }}></i>
                            Email
                        </label>
                        <input
                            type="email"
                            className="form-control"
                            minLength={3}
                            required
                            value={userInput.email || ""}
                            onChange={(e) => setUserInput({ ...userInput, email: e.target.value })}
                            placeholder="name@example.com"
                        />
                    </div>
			<div className="mb-3">
				<label for="exampleInputPassword1" className="form-label">Password</label>
				<input type="password" className="form-control" id="exampleInputPassword1" value={userInput.password || ""} onChange={(e) => setUserInput({ ...userInput, password: e.target.value })}placeholder="********"/>
			</div>
			<button type="submit" className="btn btn-primary">Submit</button>
		</form>
	);
};

