import React from 'react'
import '../styles/Button.css'

const Button = ({ head, name, type, onClick }) => {
    return (
        <h1> {head}
            <button className="button" type={type} onClick={onClick}>
                {name}
            </button>
        </h1>
    )
}

export default Button