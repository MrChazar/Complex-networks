import { Router, Route } from 'preact-router';
import MainPage from './pages/MainPage/MainPage';
import NotFoundPage from "../src/pages/NotFoundPage/NotFoundPage";

export function App() {
  return (
      <Router>
        <Route path="/" component={MainPage} />
        <Route path="/MainPage" component={MainPage} />
        <Route default component={NotFoundPage} />
      </Router>
  );
}