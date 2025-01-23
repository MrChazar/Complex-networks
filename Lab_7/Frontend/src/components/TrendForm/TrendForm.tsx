import React from 'react';
import './TrendForm.css';

const TrendForm: React.FC = () => {
    return( 
    <>
        <div>
            <form>
                <div className="form-group m-3">
                    <label htmlFor="exampleFormControlSelect1">Wypisz Tagi</label>
                    <input type="text" className="form-control"  placeholder="np. #wykop #polska" />

                    <label htmlFor="exampleFormControlSelect1">Wybierz Liczbe stron</label>
                    <input type="text" className="form-control"  placeholder="2,3,4" />
                </div>
                <button type="submit" class="btn btn-dark m-3">Wygeneruj wykres</button>
            </form>
        </div>
    </>
    );
};

export default TrendForm;
