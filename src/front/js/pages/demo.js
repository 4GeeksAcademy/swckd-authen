<<<<<<< HEAD
import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";

import { Context } from "../store/appContext";

export const Demo = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container">
			<ul className="list-group">
				{store.demo.map((item, index) => {
					return (
						<li
							key={index}
							className="list-group-item d-flex justify-content-between"
							style={{ background: item.background }}>
							<Link to={"/single/" + index}>
								<span>Link to: {item.title}</span>
							</Link>
							{// Conditional render example
							// Check to see if the background is orange, if so, display the message
							item.background === "orange" ? (
								<p style={{ color: item.initial }}>
									Check store/flux.js scroll to the actions to see the code
								</p>
							) : null}
							<button className="btn btn-success" onClick={() => actions.changeColor(index, "orange")}>
								Change Color
							</button>
						</li>
					);
				})}
			</ul>
			<br />
			<Link to="/">
				<button className="btn btn-primary">Back home</button>
			</Link>
		</div>
	);
=======
import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/demo.css";

export const Demo = () => {
    const { store, actions } = useContext(Context);
    const [userInput, setUserInput] = useState({});

    const handleSubmit = (e) => {
        e.preventDefault();
        actions.registro(userInput);
        console.log(userInput);
        window.location.href = "/";
    };

    return (
        <form onSubmit={handleSubmit} className="p-4 border rounded" style={{ maxWidth: '400px', margin: 'auto', backgroundColor: '#f8f9fa' }}>
            <h2 className="mb-4 text-center">Registro</h2>
            <div className="my-3">
                <label className="form-label d-flex align-items-center text-start">
                    <i className="fas fa-envelope mx-2" style={{ color: "#B197FC", fontSize: 24 }}></i>
                    Correo Electrónico
                </label>
                <input
                    type="email"
                    className="form-control"
                    minLength={3}
                    required
                    value={userInput.email || ""}
                    onChange={(e) => setUserInput({ ...userInput, email: e.target.value })}
                    placeholder="nombre@ejemplo.com"
                />
            </div>
            <div className="mb-3">
                <label htmlFor="exampleInputPassword1" className="form-label d-flex align-items-center text-start">
                    <i className="fas fa-lock mx-2" style={{ color: "#B197FC", fontSize: 24 }}></i>
                    Contraseña
                </label>
                <input
                    type="password"
                    className="form-control"
                    id="exampleInputPassword1"
                    value={userInput.password || ""}
                    onChange={(e) => setUserInput({ ...userInput, password: e.target.value })}
                    placeholder="********"
                />
            </div>
            <button type="submit" className="btn btn-primary w-100">Enviar</button>
        </form>
    );
>>>>>>> daeec6084f2f76cf862888ab4517a4719b87d2bc
};
