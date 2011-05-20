//
//  SampleAppAppDelegate.h
//  SampleApp
//
//  Created by 영록 on 11. 5. 19..
//  Copyright 2011 ecolemo. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface SampleAppAppDelegate : NSObject <UIApplicationDelegate> {

}

@property (nonatomic, retain) IBOutlet UIWindow *window;

@property (nonatomic, retain) IBOutlet UINavigationController *navigationController;

@end
