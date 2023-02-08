import axios from "axios"

export async function GetData() {
    const res = await axios.get(`http://group9.exceed19.online/rooms/front`)
    return res.data
}

export async function SetSwitch(id, status) {
    const res = await axios.put(`http://group9.exceed19.online/switch/${id}/${status}`)
    return res.data
}

export async function SetMode(id, status) {
    const res = await axios.put(`http://group9.exceed19.online/mode/${id}/${status}`)
    return res.data
}

export async function SetBrightness(id, status) {
    const res = await axios.put(`http://group9.exceed19.online/brightness/${id}/${status}`)
    return res.data
}