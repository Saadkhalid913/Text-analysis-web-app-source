const Navbar = (props: { about? : boolean}) => {
    return (
    <div className = "navbar">
        {props.about && <button 
                        onClick = {() => window.location.replace("/about")}
                        className = "nav-button">About the Creator →</button>}
        {!props.about && <button 
                        onClick = {() => window.location.replace("/")}
                        className = "nav-button">← Back to Editor</button>}

    </div>
    )
}
export default Navbar