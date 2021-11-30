import React from 'react';
import { Sentiment } from './@types';
import SentimentBlob from './SentimentBlob';


interface SentimentsProps {
    Sentiments: Sentiment[] | undefined;
    SendText: () => void;
}

const Sentiments = (props: SentimentsProps) => {
    if (!props.Sentiments || props.Sentiments.length < 1 ) return (
        <div className = "sentiment-wrapper">
                <button className = "analyze-button" onClick = {props.SendText}>Analyze</button>
        </div>
    )
    props.Sentiments.sort((a, b) => b.percentage - a.percentage)
    return (<div className = "sentiment-wrapper">
                {props.Sentiments.map(s => <SentimentBlob key = {s.name} sentiment = {s} />)}
                <button className = "analyze-button" onClick = {props.SendText}>Analyze</button>
            </div>)
}

export default Sentiments;


