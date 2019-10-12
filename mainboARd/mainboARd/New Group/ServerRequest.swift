//
//  ServerRequest.swift
//  mainboARd
//
//  Created by Mariusz Derezinski-Choo on 10/12/19.
//  Copyright © 2019 backupMain Enterprises. All rights reserved.
//
import Foundation

enum ServerError:Error{
    case responseProblem
    case decodingProblem
    case otherProblem
}

struct ServerRequest {
    let resourceURL : URL
    init(endpoint: String) {
        let resourceString = "http://board1331.herokuapp.com/"
        guard let resourceURL = URL(string: resourceString)else {fatalError()}
        self.resourceURL = resourceURL
    }
    func save(_ messagetoSave: Message, completion: @escaping(Result<Message, ServerError>) -> Void) {
        do{
            var urlRequest = URLRequest(url: resourceURL)
            urlRequest.httpMethod = "POST"
            urlRequest.addValue("application/json",forHTTPHeaderField: "Content-Type")
            urlRequest.httpBody = try JSONEncoder().encode(messagetoSave)
            
            let dataTask = URLSession.shared.dataTask(with: urlRequest){data, response, _ in
                
            }
        }
    }
    
    
}
