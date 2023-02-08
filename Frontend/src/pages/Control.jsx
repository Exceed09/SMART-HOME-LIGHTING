import { useState, useEffect } from "react";
import Button from '../components/Button';
import TextFormField from '../components/TextFormField';
import { GetData, SetBrightness, SetMode, SetSwitch } from "../services/Pulldata";
import "../styles/Control.css"

const Control = ({ id }) => {
    const [isOn, setIsOn] = useState(false)
    const [isAuto, setIsAuto] = useState(false)
    const [brightness, setBrightness] = useState(1)
    let statusTextOn = isOn ? "ON" : "OFF"
    let statusTextAuto = isAuto ? "Auto" : "Manual"

    useEffect(() => {
        setInterval(() => {
            GetData().then((res) => {
                res = res["message"]
                setIsOn(res[id - 1].on_status)
                setIsAuto(res[id - 1].mode_auto)
                setBrightness(res[id - 1].brightness)
            }).catch((err) => {
                console.log(err)
            })
        }, 100)
    }, [])

    return (
        <>
            <div className="con-compo">
                <h1>Room {id}</h1>
                <Button head="Status" name={statusTextOn} onClick={
                    e => SetSwitch(id, !isOn)
                } />

                <Button head="Auto" name={statusTextAuto} onClick={
                    e => SetMode(id, !isAuto)
                } />

                <TextFormField name="Brightness" value={brightness} onChange={
                    e => SetBrightness(id, int(e.target.value))
                } />
            </div>
        </>
    )
}

export default Control