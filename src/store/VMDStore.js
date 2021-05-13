import Axios from "../Repo"

const state = {
    VMDS: [],
    VMDGroups: []
}
const getters = {
    GetVMDS: (state) => state.VMDS,
    GetVMDGroups: (state) => state.VMDGroups,

}
const mutations = {
       
    mutation__addVMD(state, data){
        state.VMDS = data
    },
    mutation__addVMDGroups(state, data){
        state.VMDGroups = data
    }
}


const actions = {
    get_VMDS_ByID({commit}, query){
        commit
        return new Promise((resolve, reject) => {
            Axios.get('api/VMDS/'+query)
            .then(data => {
                commit('mutation__addVMD', data.data)

                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    get_VMDS({commit}){
        commit
        return new Promise((resolve, reject) => {
            Axios.get('api/VMDS/')
            .then(data => {
                commit('mutation__addVMD', data.data)

                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    get_VMDSGroups({commit}){
        commit
        return new Promise((resolve, reject) => {
            Axios.get('api/VMDGroups/')
            .then(data => {
                commit('mutation__addVMDGroups', data.data)

                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    post_VMDS({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.post('api/VMDS/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    patch_VMDS({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.patch('api/VMDS/'+payload.id+'/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    delete_VMDS({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.delete('api/VMDS/'+payload.id+'/')
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    get_VMDGroups({commit}){
        commit
        return new Promise((resolve, reject) => {
            Axios.get('api/VMDGroups/')
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    post_VMDGroups({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.post('api/VMDGroups/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    patch_VMDGroups({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.patch('api/VMDGroups/'+payload.id+'/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    delete_VMDGroups({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.delete('api/VMDGroups/'+payload.id+'/')
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    get_VMDConfig({commit}){
        commit
        return new Promise((resolve, reject) => {
            Axios.get('api/VMDConfig/')
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    post_VMDConfig({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.post('api/VMDConfig/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    patch_VMDConfig({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.patch('api/VMDConfig/'+payload.id+'/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
}   

export const VMDStore = {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
