import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { BackendURL } from "./component/backendURL";

import { Home } from "./pages/home";
import { Demo } from "./pages/demo";
import { Single } from "./pages/single";
<<<<<<< HEAD
=======
import {Usuario} from "./pages/usuario";
import {ResetPassword} from "./pages/ResetPassword";
import {ForgotPassword} from "./pages/ForgotPassword";
>>>>>>> daeec6084f2f76cf862888ab4517a4719b87d2bc
import injectContext from "./store/appContext";

import { Navbar } from "./component/navbar";
import { Footer } from "./component/footer";

//create your first component
const Layout = () => {
    //the basename is used when your project is published in a subdirectory and not in the root of the domain
    // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
    const basename = process.env.BASENAME || "";

    if(!process.env.BACKEND_URL || process.env.BACKEND_URL == "") return <BackendURL/ >;

    return (
        <div>
            <BrowserRouter basename={basename}>
                <ScrollToTop>
                    <Navbar />
                    <Routes>
                        <Route element={<Home />} path="/" />
<<<<<<< HEAD
                        <Route element={<Demo />} path="/demo" />
                        <Route element={<Single />} path="/single/:theid" />
                        <Route element={<h1>Not found!</h1>} />
=======
                        <Route element={<Demo />} path="/signup" />
                        <Route element={<Single />} path="/login" />
                        <Route element={<h1>Not found!</h1>} />
                        <Route element={<Usuario />} path="/private" />
                        <Route element={<ForgotPassword />} path="/forgotpassword" />
                        <Route element={<ResetPassword />} path="/resetpassword/:user_uuid" />
>>>>>>> daeec6084f2f76cf862888ab4517a4719b87d2bc
                    </Routes>
                    <Footer />
                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);
