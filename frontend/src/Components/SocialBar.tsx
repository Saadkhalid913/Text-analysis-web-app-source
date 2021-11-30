import React from 'react'
import {AiFillTwitterSquare, AiFillLinkedin, AiFillGithub} from "react-icons/ai"
const SocialBar = () => {
    return (
        <div className = "social-bar">
            <a href = "https://github.com/saadkhalid913" target = "_blank" rel="noreferrer"><AiFillGithub/></a>
            <a href = "https://twitter.com/saad89d" target = "_blank" rel="noreferrer"><AiFillTwitterSquare/></a>
            <a href = "https://www.linkedin.com/in/saad-khalid1/" target = "_blank" rel="noreferrer"><AiFillLinkedin/></a>
        </div>
    )
}

export default SocialBar