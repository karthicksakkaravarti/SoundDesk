import Axios from "../Repo"

const state = {

}
const getters = {

}
const mutations = {
    
}


const actions = {
    // RegionDimensionAndCoOrdinates
    get_RegionDimensionAndCoOrdinates({commit}, queryparam){
        commit
        return new Promise((resolve, reject) => {
            Axios.get('api/RegionDimensionAndCoOrdinates/'+queryparam)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    post_RegionDimensionAndCoOrdinates({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.post('api/RegionDimensionAndCoOrdinates/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    patch_RegionDimensionAndCoOrdinates({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.patch('api/RegionDimensionAndCoOrdinates/'+payload.id+'/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    // Schedule
    get_Schedule({commit}, queryparam){
        commit
        return new Promise((resolve, reject) => {
            Axios.get('api/Schedule/'+queryparam)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    post_Schedule({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.post('api/Schedule/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    patch_Schedule({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.patch('api/Schedule/'+payload.id+'/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    get_TextMessage({commit}, queryparam){
        commit
        return new Promise((resolve, reject) => {
            Axios.get('api/TextMessage/'+queryparam)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    post_TextMessage({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.post('api/TextMessage/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    patch_TextMessage({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.patch('api/TextMessage/'+payload.id+'/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    delete_TextMessage({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.delete('api/TextMessage/'+payload.id+'/')
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },

    //PublishManagement
    get_PublishManagement({commit}, queryparam){
        commit
        return new Promise((resolve, reject) => {
            Axios.get('api/PublishManagement/'+queryparam)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    post_PublishManagement({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.post('api/PublishManagement/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    patch_PublishManagement({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.patch('api/PublishManagement/'+payload.id+'/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    delete_PublishManagement({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.delete('api/PublishManagement/'+payload.id+'/')
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    //Playlist
    get_Playlist({commit}, queryparam){
        commit
        return new Promise((resolve, reject) => {
            Axios.get('api/Playlist/'+queryparam)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    post_Playlist({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.post('api/Playlist/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    patch_Playlist({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.patch('api/Playlist/'+payload.id+'/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    delete_Playlist({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.delete('api/Playlist/'+payload.id+'/')
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
}   

export const Messaging = {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
