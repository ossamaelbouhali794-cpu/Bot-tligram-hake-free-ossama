<?php
$token = "1770345128:AAFeE-uF4k6nEF2TnOOQd8LjPM7OoRuA2ds";
define('API_KEY',$token);
echo file_get_contents("https://api.telegram.org/bot" . API_KEY . "/setwebhook?url=" . $_SERVER['SERVER_NAME'] . "" . $_SERVER['SCRIPT_NAME']);
            function bot($method,$datas=[]){
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
$ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}
function SendChatAction($chat_id, $action)
{
    return bot('sendChatAction', [
        'chat_id' => $chat_id,
        'action' => $action
    ]);
}
function SendMessage($chat_id, $text, $parse_mode = "MARKDOWN", $disable_web_page_preview = true, $reply_to_message_id = null, $reply_markup = null)
{
    return bot('sendMessage', [
        'chat_id' => $chat_id,
        'text' => $text,
        'parse_mode' => $parse_mode,
        'disable_web_page_preview' => $disable_web_page_preview,
        'disable_notification' => false,
        'reply_to_message_id' => $reply_to_message_id,
        'reply_markup' => $reply_markup
    ]);
}
//---//
$update = json_decode(file_get_contents('php://input'));
if($update->message){
	$message = $update->message;
$message_id = $update->message->message_id;
$username = $message->from->username;
$chat_id = $message->chat->id;
$title = $message->chat->title;
$text = $message->text;
$user = $message->from->username;
$name = $message->from->first_name;
$from_id = $message->from->id;
}
if($update->callback_query){
$data = $update->callback_query->data;
$chat_id = $update->callback_query->message->chat->id;
$title = $update->callback_query->message->chat->title;
$message_id = $update->callback_query->message->message_id;
$name = $update->callback_query->message->chat->first_name;
$user = $update->callback_query->message->chat->username;
$from_id = $update->callback_query->from->id;
}
if($update->edited_message){
	$message = $update->edited_message;
	$message_id = $message->message_id;
$username = $message->from->username;
$chat_id = $message->chat->id;
$chat_id = $message->chat->id;
$text = $message->text;
$user = $message->from->username;
$name = $message->from->first_name;
$from_id = $message->from->id;
	}
	if($update->channel_post){
	$message = $update->channel_post;
	$message_id = $message->message_id;
$chat_id = $message->chat->id;
$text = $message->text;
$user = $message->chat->username;
$title = $message->chat->title;
$name = $message->author_signature;
$from_id = $message->chat->id;
	}
	if($update->edited_channel_post){
	$message = $update->edited_channel_post;
	$message_id = $message->message_id;
$chat_id = $message->chat->id;
$text = $message->text;
$user = $message->chat->username;
$name = $message->author_signature;
$from_id = $message->chat->id;
	}
	if($update->inline_query){
		$inline = $update->inline_query;
		$message = $inline;
		$user = $message->from->username;
$name = $message->from->first_name;
$from_id = $message->from->id;
$query = $message->query;
$text = $query;
		}
	if($update->chosen_inline_result){
		$message = $update->chosen_inline_result;
		$user = $message->from->username;
$name = $message->from->first_name;
$from_id = $message->from->id;
$inline_message_id = $message->inline_message_id;
$message_id = $inline_message_id;
$text = $message->query;
$query = $text;
		}
		$tc = $update->message->chat->type;
		$re = $update->message->reply_to_message;
		$re_id = $update->message->reply_to_message->from->id;
$re_user = $update->message->reply_to_message->from->username;
$re_name = $update->message->reply_to_message->from->first_name;
$re_messagid = $update->message->reply_to_message->message_id;
$re_chatid = $update->message->reply_to_message->chat->id;
$photo = $message->photo;
$video = $message->video;
$sticker = $message->sticker;
$file = $message->document;
$audio = $message->audio;
$voice = $message->voice;
$caption = $message->caption;
$photo_id = $message->photo[0]->file_id;
$video_id= $message->video->file_id;
$sticker_id = $message->sticker->file_id;
$file_id = $message->document->file_id;
$music_id = $message->audio->file_id;
$voice_id = $message->voice->file_id;
$forward = $message->forward_from_chat;
$forward_id = $message->forward_from_chat->id;
$title = $message->chat->title;
if($re){
	$forward_type = $re->forward_from->type;
$forward_name = $re->forward_from->first_name;
$forward_user = $re->forward_from->username;
	}else{
$forward_type = $message->forward_from->type;
$forward_name = $message->forward_from->first_name;
$forward_user = $message->forward_from->username;
$forward_id = $message->forward_from->id;
if($forward_name == null){
	$forward = $message->forward_from_chat;
$forward_id = $message->forward_from_chat->id;
$forward_title = $message->forward_from_chat->title;
	}
}
$title = $message->chat->title;
$admin = "1141581647";
$saiko = json_decode(file_get_contents("saiko.json"),1);
//--//
if($text == "/start"){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
*⏺l هلا حب هذا بوت الرشق
---
⛔️꒐ ملاحظة : البوت يدعم اسياسيل فقط
---
⚠️l الان اختر ما تريد من الاسفل
---
للتواصل ~
 ( tele @H1HHH <--> CH @fT7TV0 )*",
'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"🔘l شحن عن طريق كارت" ,'callback_data'=>"kart"],['text'=>"🔘l شحن عن طريق التحويل" ,'callback_data'=>"thoel"]],
[['text'=>"⚠️l الاسعار" ,'callback_data'=>"as3ar"]],
]])
]);
}
if($data == "back"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"*👋꒐ اهلا بك عزيزي
⏺️l في بوت رشق متابعين الانستاكرام
---
⛔꒐ ملاحضة : البوت يدعم اسياسيل فقط
---
⚠️l الان اختر ما تريد من الاسفل
*",
'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"🔘l شحن عن طريق كارت" ,'callback_data'=>"kart"],['text'=>"🔘l شحن عن طريق التحويل" ,'callback_data'=>"thoel"]],
[['text'=>"⚠️l الاسعار" ,'callback_data'=>"as3ar"]],
]])
]);
}
if($data == "as3ar"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
‹ رشق ضمان 
(  لمدة 100 يوم تعويض تلقائي 
يعني شكد مينزل يرجع يصعد وحدة
- جودة المتابعين ممتازة 
يضعون صور وبايو واسم 
يعني ميبينون رشق )
‹ 10$ ~ 5k
‹ 20$ ~ 10k
‹ 15k ~ 30$
‹ 40$ ~ 20k
‹ 50$ ~ 25k
‹ 60$ ~ 30k
‹ 100$ ~50k 
‹ 45K ~ 40$
‹ 50K ~ 45$
<---------->
‹ ( رشق بدون ضمان نزول قليل )
‹ 10$ ~ 6k
‹ 15$ ~ 11k
‹ 30$ ~ 25k
‹ 60$ ~50k
‹ 120$ ~ 100k
<---------->
‹ ( رشق لايكات )
‹ 3$ ~ 2k
‹ 4$ ~ 3k
‹ 5$ ~ 4k
‹ 6$ ~ 5k
<------>
‹  رشق تعليقات عربية 
( حسب الطلب )
‹ 3$ ~ 1k
‹ 5$ ~ 2k
‹ 6$ ~ 3k
‹ 8$ ~ 4k
‹ 10$ ~ 5k
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"↩️꒐ رجوع" ,'callback_data'=>"back"]],
]])
]);
}
if($data == "kart"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"✅꒐ الان ارسل رقم الكارت بسطر
🔘l ويوزر حسابك بسطر
---
⚠️l مثال
---
رقم الكارت : يوزرك
27925473997258 : ameer.8882
",
]);
$saiko[$from_id] = "kart";
file_put_contents("saiko.json",json_encode($saiko));
}
if($text and $saiko[$from_id] == "kart"){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"⏺️꒐ تم الارسال للادمن انتضر قليلا...",
'reply_to_message_id'=>$message->message_id,
]);
bot('sendmessage',[
'chat_id'=>$admin,
'text'=>"👋꒐ اهلا عزيزي الادمن
⏺️l هنالك شخص ارسل كارت ويوزر
---
@$user
---
⛔ : $text
",
]);
$saiko[$from_id] = "no";
file_put_contents("saiko.json",json_encode($saiko));
}
if($data == "thoel"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
✅꒐ الان قم بارسال المبلغ للرقم 
🔘l الرقم : 07726746845
---
⚠️l ومن ثم قم بارسال صورة الاثبات ووصفها يوزر حسابك
",
]);
$saiko[$from_id] = "thoel";
file_put_contents("saiko.json",json_encode($saiko));
}
if($message and $saiko[$from_id] == "thoel"){
bot('ForwardMessage',[
'chat_id'=>$admin,
'from_chat_id'=>$chat_id,
'message_id'=>$message->message_id,
]);
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"⏺️꒐ تم الارسال للادمن انتضر قليلا...",
'reply_to_message_id'=>$message->message_id,
]);
bot('sendmessage',[
'chat_id'=>$admin,
'text'=>"👋꒐ اهلا عزيزي الادمن
👆l هنالك شخص ارسل اثبات تحويل
---
@$user
",
]);
$saiko[$from_id] = "no";
file_put_contents("saiko.json",json_encode($saiko));
}