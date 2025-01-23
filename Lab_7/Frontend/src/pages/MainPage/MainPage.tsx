import { h } from 'preact';
import { useEffect, useState } from 'preact/hooks';
import { Link } from 'preact-router'; // Użyj Link zamiast <a>
import './MainPage.css';
import { Axios } from 'axios';
import 'bootstrap/scss/bootstrap.scss';
import * as bootstrap from 'bootstrap'
import TrendForm from '../../components/TrendForm/TrendForm'
type ApiResponse = {
    name: string;
};

const MainPage = () => {
    const [data, setData] = useState<ApiResponse | null>(null);

    useEffect(() => {
        fetch("http://localhost:8000/get-name")
            .then((response) => response.json())
            .then((data) => setData(data));
            console.log(data);
    }, []);

    return (
        <div className="App">
            <nav className="navbar" id="navbar">
                <div className="container">
                    <link rel="icon" type="image/x-icon" href="/img/favicon.ico"></link>
                    <h1>Wykop Trends</h1>
                </div>
            </nav>

            <div className="container justify-content-center align-items-center" id="content">
                <div id="ChartSelector" >
                    <TrendForm></TrendForm>
                </div>

                <div id="ChartSelector">
                    <h1>Wykres</h1>
                </div>
            </div>

            <footer className="py-3" id="footer">
                <div className="container text-center">
                    <h5>Wykonał MrChazar</h5>
                </div>
            </footer>
        </div>
    );
};

export default MainPage;