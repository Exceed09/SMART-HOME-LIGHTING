import React from 'react'
import { Link } from 'react-router-dom'
import '../styles/Card.css'
import defaultImg from '../assets/default.png'
import Button from './Button'
import Control from '../pages/Control'

const Card = ({ id }) => {
	return (
		<Control id={id}></Control>

	)
}

export default Card