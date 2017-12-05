export default function (content) {
  content = content.replace(/\\n\"/g, '<br />'); // replace all `\n"` with `<br />`
  content = content.replace(/(?:\r\\n|\r|\\n)/g, '<br />'); // replace all `\n` with `<br />`
  content = content.replace(/\\http/g, 'http'); // replace all `\http` with `http`
  return content;
} 