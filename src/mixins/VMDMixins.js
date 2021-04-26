import { mapGetters, mapActions} from 'vuex'


export const VMDMixins = {
    computed:{
        
        ...mapGetters('VMDStore', ['GetVMDS', 'GetVMDGroups']),

    },
    methods:{
        ...mapActions('VMDStore', ['get_VMDS', 'post_VMDS', 'get_VMDConfig','patch_VMDS', 'delete_VMDS',
    'get_VMDGroups', 'post_VMDGroups', 'patch_VMDGroups', 'delete_VMDGroups', 'post_VMDConfig', 'patch_VMDConfig', 'get_VMDSGroups']),

    }
}
