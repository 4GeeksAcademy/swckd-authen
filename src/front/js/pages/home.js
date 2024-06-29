import React, { useContext } from "react";
import { Context } from "../store/appContext";
<<<<<<< HEAD
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5">
			<h1>Hello Rigo!!</h1>
			<p>
				<img src={rigoImageUrl} />
			</p>
			<div className="alert alert-info">
				{store.message || "Loading message from the backend (make sure your python backend is running)..."}
			</div>
			<p>
				This boilerplate comes with lots of documentation:{" "}
				<a href="https://start.4geeksacademy.com/starters/react-flask">
					Read documentation
				</a>
			</p>
		</div>
	);
};
=======
import { Link } from "react-router-dom";
import "../../styles/home.css";

export const Home = () => {
    const { store, actions } = useContext(Context);

    return (
        <>
            <div className="cool-image-container text-center mt-5">
                <img 
                    src="https://pbs.twimg.com/media/EnIvENHWEAEyeZv.jpg" 
                    alt="Cool" 
                    className="cool-image img-fluid rounded"
                />
            </div>
            <div className="botones d-flex justify-content-around mt-4">
                <Link to="/signup">
                    <button className="btn btn-primary">Llévame al registro jefe</button>
                </Link>
                <Link to="/login">
                    <button className="btn btn-secondary">Llévame al login máquina</button>
                </Link>
            </div>
        </>
    );
};

>>>>>>> daeec6084f2f76cf862888ab4517a4719b87d2bc
