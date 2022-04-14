import os
import re
import shutil

new_code ="""yA=(n(3904),o.a.initNS("im.recall")),bA=function(e){function t(t){var n=e.call(this,t)||this;return n.state={serverTime:void 0},n.reeditRecallMessage=n.reeditRecallMessage.bind(n),n}return Object(r.d)(t,e),t.prototype.render=function(){var e=_n.getInstance().getLemonGrayV2Boolean(qt.IM,G.a.DISABLE_CHECK_BUBBLE_SIZE_FRONTEND);this.props.onBubbleSizeChange&&!e&&this.props.onBubbleSizeChange();var t,n=this.props,r=n.isMyMsg,a=n.RecallName,i=n.msg,o=rp(i.baseMessage.content.contentType);o=rp(i.baseMessage.content.contentType);var tip_message_prefix=" ";if(i.baseMessage.shieldStatus===jt.N.YES){tip_message_prefix=" 被超管"}var l=void 0;l=o?"dt_message_recall_message_file_format":"pc_im_recalled_a_message";var s=E.i18next.t(l);try{if(i.baseMessage.content.contentType==2){s=tip_message_prefix+"撤回的图片为: "+(i.baseMessage.content.photoContent.filename==""?i.baseMessage.content.photoContent.mediaId:i.baseMessage.content.photoContent.filename);t=x.createElement("div",{className:"ding-attachment-image-wrap"},x.createElement("img",{src:i.baseMessage.content.photoContent.blurredFilePath,onClick:function(){var nx="";try{nx=dl(i.baseMessage.content.photoContent.mediaId,{imageSize:"origin",queryParams:{bizType:il.im}}).url}catch(image_exception){nx=t.mediaId}return dingtalk.message.openImageViewerWithUrl(nx,[])}}),x.createElement("div",{className:"content-wrapper"},x.createElement("span",null,a," ",s)))}else if(i.baseMessage.content.contentType==3){s=tip_message_prefix+"撤回的语音为: [请复制到浏览器打开] ";t=x.createElement("div",{className:"ding-attachment-link-wrap"},x.createElement("span",null,a," ",s),x.createElement("a",{className:"ding-attachment-link attachment-wrap",href:i.baseMessage.content.audioContent.url,target:"_blank"},i.baseMessage.content.audioContent.url))}else if(i.baseMessage.content.contentType==102){s=tip_message_prefix+"撤回的网址为: "+i.baseMessage.content.attachments[0].extension.title+" ";t=x.createElement("div",{className:"ding-attachment-link-wrap"},x.createElement("span",null,a," ",s),x.createElement("a",{className:"ding-attachment-link attachment-wrap",href:i.baseMessage.content.attachments[0].extension.source_url,target:"_blank"},i.baseMessage.content.attachments[0].extension.source_url))}else if(i.baseMessage.content.contentType==501){s=tip_message_prefix+"撤回的文件为: "+i.baseMessage.content.attachments[0].extension.f_name;t=x.createElement("span",null,a," ",s)}else if(i.baseMessage.content.contentType==1200){s=tip_message_prefix+"撤回的消息为: "+i.baseMessage.content.attachments[0].extension.title;t=x.createElement("span",null,a," ",s)}else if(i.baseMessage.content.contentType==3100){s=tip_message_prefix+"撤回的富文本消息为: "+i.baseMessage.content.attachments[0].extension.desc;t=x.createElement("span",null,a," ",s)}else{s=tip_message_prefix+"撤回的消息为: "+(i.baseMessage.content.extension!=null&&i.baseMessage.content.extension.sp_fName!=null?i.baseMessage.content.extension.sp_fName:i.baseMessage.content.textContent.text);t=x.createElement("span",null,a," ",s)}}catch(message_exception){s=" 读取撤回消息失败: "+JSON.stringify(i.baseMessage);t=x.createElement("span",null,a," ",s)};return x.createElement("div",{className:"msg-recall-hint","data-msg-id":i.baseMessage.messageId},t,this.renderReEdit())},t.prototype.renderReEdit=function(){var e,t,n,r,a,i=this;if(this.state.serverTime){var o=this.props,l=o.isMyMsg,s=o.msg,u=this.state.serverTime,c=Ua()(s,"baseMessage.extension.recallMessageTime")||"";if(true){var d=Sp(s.baseMessage.content)||kp(s),f=function(e){return e.baseMessage.content.contentType===jt.A.RICH_TEXT_MSG}(s);if(function(e){return Ua()(e,"baseMessage.content.contentType")===jt.A.TEXT&&"code_snippet"!==(Ua()(e,"baseMessage.extension.text_type")||"")}(s)||f||d)return x.createElement("a",{className:"msg-recall-hint-re-edit",href:"javascript:void(0)",onClick:this.reeditRecallMessage,target:"_blank"},E.i18next.t(l?"pc_im_recalled_a_message_reedit":"查看"))}}else this.props.getServerTime().then((function(e){i.setState({serverTime:e})})).catch((function(e){yA.error(e),i.setState({serverTime:Date.now()+""})}));return null},t.prototype.reeditRecallMessage=function(e){e.preventDefault();var t=Ua()(this.props.msg,"baseMessage.conversationId"),n=Ua()(this.props.msg,"baseMessage.messageId");t&&t&&Ws(t,n)},t}(x.PureComponent),CA=function(e)"""

code_regex = 'yA=\(n\(3904\),o\.a\.initNS\("im\.recall"\)\),bA=function\(e\){[\s\S]+}\(x\.PureComponent\),CA=function\(e\)'

version_file = "/Applications/DingTalk.app/Contents/Info.plist"

chatbox_index_file = '/Applications/DingTalk.app/Contents/Resources/webcontent/assets/chatbox-index.js'
# chatbox_index_file = '/Users/zhouhui/www/dingding_duibi/chatbox-index_old.js'



version = ""
with open(version_file, 'r',encoding='utf8') as file_to_read:
    while True:
        lines = file_to_read.readline()  # 整行读取数
        if "CFBundleShortVersionString" in lines:
            version += next(file_to_read)
            break

version_regex = '<string>(.+?)<\/string>'
version = re.findall(version_regex,version)[0]
res = os.path.exists("/System/Library/CoreServices/SystemVersion.plist")
if res == False:
    print("您不是MACOS系统！")
if version != "6.5.0":
    print("您不是6.5.0版本的钉钉，请升级")
    exit(0)


shutil.copy(chatbox_index_file, r'/tmp/chatbox-index.js')

new_content = ""
with open(chatbox_index_file, 'r') as f:
    old_code = f.read()
    strinfo = re.compile(code_regex)
    new_content +=  strinfo.sub(new_code, old_code)

with open(chatbox_index_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("防撤回以安装，请重启钉钉,备份文件: /tmp/chatbox-index.js")