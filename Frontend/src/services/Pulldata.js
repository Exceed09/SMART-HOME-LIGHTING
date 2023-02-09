import axios from "axios"

export async function GetData() {
    const res = await axios.get(`https://ecourse.cpe.ku.ac.th/exceed09/rooms/front`)
        // const res = await axios.get(`http://group9.exceed19.online/rooms/front`)
    return res.data
}

export async function SetSwitch(id, status) {
    const res = await axios.put(`https://ecourse.cpe.ku.ac.th/exceed09/switch/${id}/${status}`)
        // const res = await axios.put(`http://group9.exceed19.online/switch/${id}/${status}`)
    return res.data
}

export async function SetMode(id, status) {
    const res = await axios.put(`https://ecourse.cpe.ku.ac.th/exceed09/mode/${id}/${status}`)
        // const res = await axios.put(`http://group9.exceed19.online/mode/${id}/${status}`)
    return res.data
}

export async function SetBrightness(id, status) {
    if (status < 1) {
        status = 1
    }
    if (status > 255) {
        status = 255
    }
    const res = await axios.put(`https://ecourse.cpe.ku.ac.th/exceed09/brightness/${id}/${status}`)
    return res.data
}