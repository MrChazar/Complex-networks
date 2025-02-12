import { h } from 'preact';
import { useState } from 'preact/hooks';
import './TrendForm.css';

interface FormData {
  tags: string;
  pages: number;
}

interface FormComponentProps {
    onSubmit: (formData: FormData) => void; 
}

const TrendForm : React.FC<FormComponentProps> = ({ onSubmit }) => {
  const [formData, setFormData] = useState<FormData>({
    tags: '',
    pages: 0,
  });

  const handleInputChange = (e: Event) => {
    const target = e.target as HTMLInputElement;
    setFormData({
      ...formData,
      [target.name]: target.value,
    });
  };

  const validateForm = () => {
    return formData.pages !== 0 && formData.tags.trim() !== '';
  };

  const handleSubmit = (e: Event) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div className="form-group m-3">
          <label htmlFor="tags">Wypisz Tagi</label>
          <input
            type="text"
            className="form-control"
            name="tags"
            value={formData.tags}
            onChange={handleInputChange}
            placeholder="np. #wykop #polska"
          />

          <label htmlFor="pages">Wybierz Liczbę stron</label>
          <input
            type="number"
            className="form-control"
            name="pages"
            value={formData.pages}
            onChange={handleInputChange}
            placeholder="2, 3, 4"
          />
        </div>
        <button type="submit" className="btn btn-dark m-3">
            Wygeneruj podsumowanie
        </button>
      </form>
    </div>
  );
};

export default TrendForm;