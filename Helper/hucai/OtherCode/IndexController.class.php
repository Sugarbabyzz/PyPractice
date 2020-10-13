<?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends Controller {
    public function index(){
        $tb = D('html');
        if(I('post.action')=='gethtml'){
            $rs = $tb -> find(I('post.id'));
            $this -> success($rs);
            return false;
        }
        $map['type'] = 'province';
        $rs = $tb -> where($map) -> order(' `flag` asc ') -> select();
        $this -> assign('rs', $rs);
        $this -> display();
    }


    public function city(){
        $tb = D('city');
        $rs = $tb -> select();
        $this -> assign('rs', $rs);
        $this -> assign('table', 'county');
        $this -> assign('total', count($rs));
        $this -> display();
    }

    public function county(){
        $tb = D('county');
        $rs = $tb -> select();
        $this -> assign('rs', $rs);
        $this -> assign('table', 'town');
        $this -> assign('total', count($rs));
        $this -> display('Index/city');
    }

    public function town(){
        $tb = D('town');
        $rs = $tb -> select();
        $this -> assign('rs', $rs);
        $this -> assign('table', 'village');
        $this -> assign('total', count($rs));
        $this -> display('Index/city');
    }


    public function save(){
        $table = I('get.table');
        $tb = D($table);

        $data = I('post.save');

        //unset($data['table']);
        $rs = $tb -> addAll($data );
        $this -> success($rs);
    }




    public function js(){
        $this->display();
    }

    function GetFile($url,$way=1,$coding){
        if($way==1){
            $str=file_get_contents($url);
        }else if($way==2){
/*            @$ch=curl_init();
            curl_setopt($ch,CURLOPT_URL,$url);
            curl_setopt($ch,CURLOPT_HEADER,0);
            curl_setopt($ch,CURLOPT_NOBODY,false);
            curl_setopt($ch,CURLOPT_TIMEOUT,3);
            curl_setopt($ch,CURLOPT_FOLLOWLOCATION,true);
            curl_setopt($ch,CURLOPT_MAXREDIRS,20);
            curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
            curl_setopt($ch,CURLOPT_USERAGENT, "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.0)");
            $orders=@curl_exec($ch);
            @curl_close($ch);
            $str=$orders;*/




            $szUrl = $url;
            $UserAgent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506; .NET CLR 3.5.21022; .NET CLR 1.0.3705; .NET CLR 1.1.4322)';
            $curl = curl_init();
            curl_setopt($curl, CURLOPT_URL, $szUrl);
            curl_setopt($curl, CURLOPT_HEADER, 0);  //0表示不输出Header，1表示输出
            curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
            curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
            curl_setopt($curl, CURLOPT_ENCODING, '');
            curl_setopt($curl, CURLOPT_USERAGENT, $UserAgent);
            curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
            $data = curl_exec($curl);
            $str = $data;
            //echo $str;
        }
        if($coding=="1"){
            $str=iconv("UTF-8", "GBK", $str);
        }elseif ($coding=="2"){
            $str=iconv("GBK", "UTF-8", $str);
        }
        return $str;
    }

    public function url(){
        $url = I('get.url');
        if($url==''){
            $this -> error('url empty');
            return false;
        }

        $tb = D('html');
        $map['url'] = $url;
        $rs = $tb -> where($map) -> find();
        if($rs){
            $flag = true;
            $html = $rs['html'];
        }
        else{
            $flag = false;
            $html = $this -> GetFile($url, 2, 2);
            $html = str_replace("charset=gb2312", "charset=utf8", $html);
            if($html!=''){
                $data['url'] = $url;
                $data['html'] = $html;
                $tb -> add($data);
            }

        }

        $rs['flag'] = $flag;
        $rs['html'] = $html;
        $rs['url'] = $url;

        $this -> success($rs);
    }
}