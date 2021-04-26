import Axios from "../Repo"

const state = {
    Users : null,
    CurrentUser: null
}
const getters = {
    GetCurrentUser: (state) => state.CurrentUser,

}
const mutations = {
    mutation__currentuser(state, data){
        state.CurrentUser = data
    }
}


const actions = {
    get_Users({commit}){
        commit
        return new Promise((resolve, reject) => {
            Axios.get('api/Users/')
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    get_Curentuser({commit}){
        commit
        return new Promise((resolve, reject) => {
            Axios.get('api/Users/currentuser/')
            .then(data => {
                commit('mutation__currentuser', data.data)
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    post_Users({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.post('api/Users/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    patch_Users({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.patch('api/Users/'+payload.id+'/', payload)
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
    delete_Users({commit}, payload){
        commit
        return new Promise((resolve, reject) => {
            Axios.delete('api/Users/'+payload.id+'/')
            .then(data => {
                resolve(data)
            })
            .catch(err =>{
                reject(err)
            })
        })
    },
}   

export const UserStore = {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
