import { mapGetters,   mapActions} from 'vuex'


export const UsersMixins = {
    computed:{
        ...mapGetters('UserStore', ['GetCurrentUser']),

    },
    methods:{
        ...mapActions('UserStore', ['get_Users', 'post_Users', 'patch_Users', 'delete_Users', 'get_Curentuser']),

    }
}
