import { h } from 'preact';
import { useEffect, useState } from 'preact/hooks';
import { Link } from 'preact-router'; // Użyj Link zamiast <a>
import './MainPage.css';
import axios from 'axios';
import 'bootstrap/scss/bootstrap.scss';
import * as bootstrap from 'bootstrap'
import TrendForm from '../../components/TrendForm/TrendForm'
import TrendResult from '../../components/TrendResult/TrendResult';

interface FormData {
    tags: string;
    pages: number;
}

interface FormResponse{
    trends: string;
    image: string;
}

const MainPage = () => {
    const [formResponse, setFormResponse] = useState<FormResponse | null>(null);
    const [loadingResponse, setLoadingResponse] = useState<boolean>(false);
    const [error, setError] = useState<boolean>(false);

    const onSubmit = (formData: FormData) => {
        alert(`Wysłano formularz z tagami: ${formData.tags} i liczbą stron: ${formData.pages}`);
        setLoadingResponse(true);
        setFormResponse(null)
        setError(false)
        axios.get(`http://localhost:8000/trend/combined`, {
            params: {
                tag_name: formData.tags,
                number_of_pages: formData.pages
            }
          })
          .then(response => {
            setFormResponse(response.data);
            console.log(response.data);
            setLoadingResponse(false);
          })
          .catch(error => {
              console.error("Błąd Axios:", error);
              setLoadingResponse(false);
              setError(true);
          });
        
    };

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
                    <TrendForm onSubmit={onSubmit}></TrendForm>
                </div>

                <div id="ChartSelector">
                    {loadingResponse ? <h1>Ładowanie...</h1>: null}
                    {error ? <h1 className="text-danger">Wystąpił błąd: {error}</h1>: null}
                </div>

                {formResponse ? <>
                <div id="ChartSelector">
                    <h1>Aktualne trendy</h1> 
                    <TrendResult text={formResponse.trends}></TrendResult>
                </div>
                <div id="ChartSelector">
                    <h1>Word Cloud</h1>
                    <img src={`data:image/png;base64,${formResponse.image}`} alt="WordCloud"  />
                </div>
                </>: null}
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