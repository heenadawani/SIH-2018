<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Input;
use DB;

class UploadControllers extends Controller
{
    public function upload(){

		if(Input::hasFile('file')){
			$file = Input::file('file');
			$name = $file->getClientOriginalName();
			DB::insert("insert into xray (image_link,ctr,view) values('uploads/$name',50,'AP')");
			$file->move('uploads', $name);
			echo 'Uploaded in the database.';	
		}

	}
}
