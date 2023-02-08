import axios from "axios"

export async function GetData() {
    const res = await axios.get(`http://group9.exceed19.online/exceed09/rooms/front`)
    return res.data
}

export async function SetSwitch(id, status) {
    const res = await axios.put(`http://group9.exceed19.online/exceed09/switch/${id}/${status}`)
    return res.data
}

export async function SetMode(id, status) {
    const res = await axios.put(`http://group9.exceed19.online/exceed09/mode/${id}/${status}`)
    return res.data
}

export async function SetBrightness(id, status) {
    const res = await axios.put(`http://group9.exceed19.online/exceed09/brightness/${id}/${status}`)
    return res.data
}