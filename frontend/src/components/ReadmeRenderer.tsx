import React from 'react';
import ReactDOM from 'react-dom';
import ReactMarkdown from 'react-markdown';
// @ts-ignore
import readmeContent from '../../../README.md?raw';

const ReadmeRenderer: React.FC = () => {
    const container = document.getElementById('container');

    if (!container) return null;

    return ReactDOM.createPortal(
        <ReactMarkdown>{readmeContent}</ReactMarkdown>,
        container
    );
};

export default ReadmeRenderer;
