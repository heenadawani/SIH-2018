<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Input;

class UploadControllers extends Controller
{
    public function upload(){

		if(Input::hasFile('file')){

			echo 'Uploaded';
			$file = Input::file('file');
			$file->move('uploads', $file->getClientOriginalName());
		}

	}
}
