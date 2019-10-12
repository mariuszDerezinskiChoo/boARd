//
//  MenuView.swift
//  mainboARd
//
//  Created by Steven Chen on 10/12/19.
//  Copyright © 2019 backupMain Enterprises. All rights reserved.
//

import SwiftUI

struct MenuView: View {
    var body: some View {
        List {
            Text("main")
            Text("backupMain")
            Text("2x2 main")
            Text("2x2 backupMain")
        }
    }
}

struct SideMenu: View {
    let width: CGFloat
    let isOpen: Bool
    let menuClose: () -> Void
    
    var body: some View {
        Text("hello")
    }
    
}

struct MenuView_Previews: PreviewProvider {
    static var previews: some View {
        MenuView()
    }
}
