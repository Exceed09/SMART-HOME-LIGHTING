import { useState } from "react";
import Button from '../components/Button';
import TextFormField from '../components/TextFormField';

const Control = () => {
    const [isOn, setIsOn] = useState(false)
    const [isAuto, setIsAuto] = useState(false)
    const [brightest, setBrightest] = useState(0)
    let statusTextOn = isOn ? "ON" : "OFF"
    let statusTextAuto = isAuto ? "Auto" : "Manual"

    return (
        <>
            <Button head="Status" name={statusTextOn} onClick={
                e => setIsOn(!isOn)
            } />

            <Button head="Auto" name={statusTextAuto} onClick={
                e => setIsAuto(!isAuto)
            } />

            <TextFormField name="Brightest" value={brightest} onChange={e => setBrightest(e.target.value)} />

        </>
    )
}

export default Control