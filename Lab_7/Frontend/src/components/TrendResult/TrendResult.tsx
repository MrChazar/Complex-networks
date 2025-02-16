import React from 'react';

interface trendResultProps {
    text: string | null;
}

const TrendResult: React.FC<trendResultProps> = (props) => {
    return (
        <div>
            <p>{props.text}</p>
        </div>
    );
};

export default TrendResult;