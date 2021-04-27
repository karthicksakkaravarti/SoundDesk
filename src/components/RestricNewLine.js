import { Extension, Plugin } from 'tiptap'

export default class EnterHandler extends Extension {

  get name() {
    return 'enter_handler'
  }

  get plugins() {
    return [
      new Plugin({
        props: {
          handleKeyDown: (view, event) => {
            if (event.key === 'Enter' && !event.shiftKey) {
              // do something
              return true
            }

            return false
          },
        },
      }),
    ]
  }

}