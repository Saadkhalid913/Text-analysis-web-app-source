import {useState} from 'react';
import { toast } from 'react-toastify';
import { Sentiment } from './Components/@types';
import Homepage from './Components/Homepage';
import axios from "axios"
import { Route,Routes, BrowserRouter } from "react-router-dom"
import About from './Components/Aboutpage';
import 'react-toastify/dist/ReactToastify.css';

toast.configure()


const URI = process.env.NODE_ENV === "production" ? "/" : "http://localhost:5001/"

function App() {
  const [text, setText] = useState("")
  const DefaultSentiments = [{'name': 'anger', 'percentage': 0},
                             {'name': 'fear', 'percentage': 0},
                             {'name': 'joy', 'percentage': 0}, 
                             {'name': 'love', 'percentage': 0}, 
                             {'name': 'sadness', 'percentage': 0}, 
                             {'name': 'surprise', 'percentage': 0}]
  const [sentiments, setSentiments] = useState<Sentiment[]>(DefaultSentiments);
  



  const SendText = async () => {
    console.log("sending text")
    if (text.length === 0) {
      setSentiments(DefaultSentiments)
      return
    }

    await axios.post(URI + "sentiment", {text: text})
      .then((r: any) => {
        setSentiments(r.data.sentiments)
          console.log(r.data.sentiments)
        })
      .catch((err: any) => toast.error("There was an error connecting to the servers :("))
  }  


  return (
    // @ts-ignore
    <BrowserRouter>
    <Routes>
      <Route path = "/about" element = {<About />} />
      <Route path = "/" element = {<Homepage  Sentiments = {sentiments} setText = {setText} SendText = {SendText}/>} />
    </Routes>
    </BrowserRouter>
  )
}

export default App;