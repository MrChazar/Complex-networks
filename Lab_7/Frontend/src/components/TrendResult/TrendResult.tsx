import React from 'react';

interface trendResultProps {
    text: string | null;
}

const TrendResult: React.FC<trendResultProps> = (props) => {
    return (
        <div>
            <p style="white-space: pre-wrap;text-align: justify">{props.text}</p>
        </div>
    );
};

export default TrendResult;