import React, { useState } from 'react'
import '../styles/PlaceForm.css'

const TextFormField = ({ name, value, onChange }) => {
    return (
        <div className="form-field">
            <label>{name}</label>
            <input className="input-field" type="number" value={value} onChange={onChange} />
        </div>
    )
}

export default TextFormField