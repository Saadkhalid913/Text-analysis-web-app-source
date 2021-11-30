import React from 'react'
import RichEditorExample from './RichTextEditor'


interface TextEditorProps {
    onTextChange: (text: string) => void;
}

const TextEditor = (props: TextEditorProps) : JSX.Element => {
    return <RichEditorExample onChange = {(s:any) => {
            props.onTextChange(s)
    }}  />
} 

export default TextEditor
