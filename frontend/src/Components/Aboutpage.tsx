import React from 'react'
import Navbar from './Navbar'
import pfp from "../profile-pic.webp"
import SocialBar from './SocialBar'
const About = () => {
    return (
        <div className = "about-page">
            <Navbar />
            <div className = "about-page-content">
            <img src = {pfp} className = "pfp" alt = "saad khalid"/>
            <div className = "short-intro">
                Hi! 👋 My name is Saad. I'm a 17 year old web developer + AI/ML enthusiast. If you liked this app, 
                check out some of my other projects, and connect with me on socials!👇 Personal portfolio 👉 
                <a href = "https://saadkhalid.ca" target = "_blank" rel = "noreferrer">Here</a>
            </div>    
            <SocialBar />
            </div>
        </div>
    )
}

export default About