import React from 'react'//@ts-ignore
import { Progress } from 'react-sweet-progress';
import "react-sweet-progress/lib/style.css";


const SentimentColours : any = {
    "anger": "red",
    "fear": "orange",
    "joy": "purple",
    "love": "pink",
    "sadness": "skyBlue",
    "surprise": "yellow",
}

const SentimentBlob = (props: {sentiment: { name: string, percentage: number }}) => {
    const percent = Math.floor((props.sentiment.percentage * 100))
    const {name } = props.sentiment
    return (
        <div className = "sentiment-blob">
            <h3>{name}</h3>
            <Progress 
            theme = {{
                    default: {
                        color: SentimentColours[name]
                    },
                    active :{
                        color: SentimentColours[name]
                    }
                    
                }
            }
            percent = {percent}/>
        </div>
    )
}

export default SentimentBlob